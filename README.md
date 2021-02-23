# 帮张臻昊小朋友做的练习 

## 思路
其次我对 tk 也不熟悉， 但是根据小张的描述以及查询资料，写下解决问题的思路，应该能解决这个issue

1. mainwindow, 是全局变量，所以在各个函数里都能调用
2. 不同函数里的局部变量， 不能相互访问，所以loginwindow要传给check函数destroy
3. 不知道一个函数怎么用，没关系
    - 用关键字去搜索， 比如我要干掉一个窗口，我就会想 disapear disable hide vanish等单词，然后加上tkinter 去用google搜索
    - 写代码的软件里有些快捷键，能帮你找到定义，甚至找出用法
4. 整体的思路
    - 主窗口上放入button
    - button和一个函数bind， callup 一个新窗口
    - 新窗口上放入entry， label等， 根据提示去做操作
    - 选中正确的对像后，当前窗口消失，让一新窗口出现

