# 介绍
一个在线的Wasm程序分析工具，包含两个功能
- [wasm2c](https://github.com/WebAssembly/wabt)
- [反编译](https://github.com/nneonneo/ghidra-wasm-plugin/)

# 使用
```
docker build -t wasm-rev-online .
docker run -p 5000:5000 wasm-rev-online
```

# refs
代码高亮来自于
[prettify](https://github.com/hongrunhui/prettify.js.git)
[install ghidra plugin in headless mode](https://github.com/astrelsky/Ghidra-Cpp-Class-Analyzer/issues/43)