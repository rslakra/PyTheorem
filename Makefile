#
# Author: Rohtash Lakra
#
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in
# the 'Makefile' there's top-level Makefile-only syntax, and everything else is bash script syntax.
# The ${} notation is specific to the make syntax and is very similar to bash's $()
#
# Signifies our desired python version
# PYTHON = python3
# https://gist.github.com/MarkWarneke/2e26d7caef237042e9374ebf564517ad
#
VENV := venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
REMOVE_FILES := __pycache__

# Default values
TEST_DIR ?= tests
PATTERN ?= test*.py
TOP_DIR ?= .
VERBOSE ?= -v

# Makefile configs for Sphinx documentation
# You can set these variables from the command line, and also from the environment for the first two.
#
# SPHINXOPTS    ?=
# SPHINXBUILD   ?= sphinx-build
# SOURCEDIR     = .
# BUILDDIR      = build

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY: help
# .PHONY: help Makefile

# Defining an array variable
# FILES = input output

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified
# commands. This target is executed whenever we just type `make`
.DEFAULT_GOAL := help

# all operations
all: help


# The @ makes sure that the command itself isn't echoed in the terminal
# Put it first so that "make" without argument is like "make help".
# Catch-all target: route all unknown targets
#help:
#	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

define find.functions
	@# @fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
    @printf "%-25s %s\n" "Target" "Description"
    @printf "%-25s %s\n" "----------------" "----------------"
    @make -pqR : 2>/dev/null \
        | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' \
        | sort \
        | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' \
        | xargs -I _ sh -c 'printf "%-25s " _; make _ -nB | (grep -i "^# Help:" || echo "") | tail -1 | sed "s/^# Help: //g"'
endef

# A hidden target
.hidden:

help:
	@echo
	@echo 'The following commands can be used:'
	@echo
	$(call find.functions)
	@echo

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# This generates the desired project file structure
# A very important thing to note is that macros (or makefile variables) are referenced in the target's code with a single dollar sign ${}, but all script variables are referenced with two dollar signs $${}
# setup:
#     @echo "Checking if project files are generated..."
#     [ -d project_files.project ] || (echo "No directory found, generating..." && mkdir project_files.project)
#     for FILE in ${FILES}; do \
#         touch "project_files.project/$${FILE}.txt"; \
#     done

setup: ## Sets up environment and installs requirements
setup:
	@# Help: Sets up environment and installs requirements
	@echo "Setting up the Python environment ..."
	python3 -m pip install virtualenv
	python3 -m $(VENV) $(VENV)
	#source $(VENV)/bin/activate
	. $(VENV)/bin/activate
	@echo
	(pwd)
	@echo
	$(PIP) install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# In this context, the *.project pattern means "anything that has the .project extension"
clean: ## Remove build and cache files
clean:
	@# Help: Remove build and cache files
	@echo "Cleaning up ..."
	#$(VENV)/bin/deactivate
	#deactivate
	@echo "Removing $(VENV)"
	rm -rf $(VENV)
	rm -rf $(REMOVE_FILES) *.project
	find . -name '*.py[co]' -delete
	find . -type f -name '*.py[co]' -delete

venv: ## Activates the virtual environment
venv:
	@# Help: Sets up environment and installs requirements
	@echo "Activating Virtual Environment ..."
	source $(VENV)/bin/activate

flask-app: ## Runs the python application
flask-app: venv
	@echo "Running Python Application ..."
	@$(PYTHON) -m flask --app wsgi run --port 8080 --debug

# The ${} notation is specific to the make syntax and is very similar to bash's $()
# This function uses unittest to test our source files
unittest: ## Tests the python application
unittest:
	@echo "Running Python [unittest] ..."
	#@$(PYTHON) -m unittest discover -s tests -p "test*.py" -t . -v
	@$(PYTHON) -m unittest
	-#find coverage/ -mindepth 1 -delete
#	pytest $${TESTS}
#	@$(PYTHON) setup.py sdist

# This function uses pytest to test our source files
pytest: ## Tests the python application
pytest:
	@echo "Running Python [pytest] ..."
	@$(PYTHON) -m pytest
	-#find coverage/ -mindepth 1 -delete

# Example Usage
# make test                                # default
# make test PATTERN=test_math_*.py         # run only math-related tests
# make test TEST_DIR=subtests TOP_DIR=.    # custom test folder
# To exit immediately on first failure, you can change the runner in the Makefile:
#@$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "$(PATTERN)" -t $(TOP_DIR) $(VERBOSE) || exit 1

test: ## Tests the python application
test:
	@# Help: Tests the python application
	@echo "Testing Python Application ..."
	@echo
	@echo "Running tests from [$(TEST_DIR)], pattern=[$(PATTERN)], rootDir=[$(TOP_DIR)] ..."
	@echo
	@$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "$(PATTERN)" -t $(TOP_DIR) $(VERBOSE)

docs: ## Generates the documentation
docs:
	${PYTHON} setup.py build_sphinx
	@echo
	@echo Generated documentation: "file://"$$(readlink -f doc/build/html/index.html)
	@echo

dist: ## Distributes the application
dist: test
	@# Help: Distributes the application
	python setup.py sdist

lint: ## Runs the application, exit if critical rules are broken
lint:
	@# Help: Runs the application, exit if critical rules are broken
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src --count --exit-zero --statistics
