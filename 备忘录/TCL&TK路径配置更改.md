# 背景
**SUAVE**内部自动检测系统路径的**TCL_LIBRARY**和**TK_LIBRARY**，该路径为**CFD++**安装时添加，但版本与**p36**环境不同，因此删除这两个路径以使用**SUAVE**
# 具体操作
编辑系统环境变量
删除以下两条
**TCL_LIBRARY
TK_LIBRARY**
# 恢复方法
创建环境变量
**TCL_LIBRARY=E:\CFDPLUS\METACOMP\mlib\tcltk8\lib\tcl8.4**
**TK_LIBRARY=E:\CFDPLUS\METACOMP\mlib\tcltk8\lib\tk8.4**