## rCore_tutorial_v3 TESTS

本项目用于为 rCore 实验进行 CI 测试，在 user 目录下 `make all CHAPTER=x` 可获得第 x 章的测例。

- 可选项 2, 3_0, 3_2, 4, 5, 6, 7。

**重要**-加载地址更新：

- chapter2 所有程序加载位置位于 0x80400000，与示例代码一致。
- chapter3 测试程序分为 3 批，每一批的地址都为 0x80400000 + id\*0x20000，id 为程序在这一批中的序号。每一批都与参考代码一致，请分别测试。
- chapter4-7 所有程序加载位置位于 0x0，与示例代码一致。

可以在 `user/build/asm` 目录下查看汇编来确认加载地址。

**测例更新**

- 一部分无用测例已删除，包括 ch2_helloworld, ch3_1_yield 等。
- sleep 测例被转移到第四章