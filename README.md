# sd-webui-pe
2023/11/04:

Fooocus V2动态提示功能的Webui移植，安装之后首次运行会自动从 https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_expansion.bin 下载GPT-2模型，并保存到 .\extensions\sd-webui-pe\scripts\expansion\pytorch_model.bin

如果自动下载失败，可以自己手动下载。

安装成功只要勾选启动就会生效。
![image](https://github.com/facok/sd-webui-pe/assets/128763816/190e036d-bf40-418b-80eb-14bb1971ca3d)

启用前：
![image](https://github.com/facok/sd-webui-pe/assets/128763816/9f53af4f-2d5c-4490-bcb9-72f43da28416)

启用后：
![image](https://github.com/facok/sd-webui-pe/assets/128763816/39ee44c4-eed3-4e85-b4c8-d3e0692c85f7)

关于Fooocus V2原版功能介绍：
https://github.com/lllyasviel/Fooocus/discussions/117#raw
