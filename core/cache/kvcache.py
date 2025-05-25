# import time
#
# import numpy as np
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
#
# # Reference:
# # https://medium.com/@joaolages/kv-caching-explained-276520203249
# # https://neptune.ai/blog/transformers-key-value-caching
#
#
# device = "cuda" if torch.cuda.is_available() else "cpu"
# tokenizer = AutoTokenizer.from_pretrained("gpt2")
# model = AutoModelForCausalLM.from_pretrained("gpt2").to(device)
#
# for use_cache in (True, False):
#     times = []
#     for _ in range(10):  # measuring 10 generations
#         start = time.time()
#         model.generate(**tokenizer("What is KV caching?", return_tensors="pt").to(device),
#                        use_cache=use_cache,
#                        max_new_tokens=1000)
#         times.append(time.time() - start)
#     print(
#         f"{'with' if use_cache else 'without'} KV caching: {round(np.mean(times), 3)} +- {round(np.std(times), 3)} seconds")
