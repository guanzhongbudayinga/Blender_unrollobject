# Blender_unrollobject
这是用 Python 编写的脚本，专门用于 Blender 中的 bmesh 模块，也就是 Blender 的网格编辑 API。

#具体解释：

* `import bpy`, `import bmesh`: 引入 Blender 的 Python 接口。
* `context = bpy.context`：获取当前的 Blender 上下文。
* `bmesh.from_edit_mesh(me)`：从编辑模式的网格数据创建一个 bmesh。
* `bmesh.ops.bisect_plane(...)` 和 `bmesh.ops.split_edges(...)`: 分别是进行平面切割与边拆分的 bmesh 操作。
* `Vector`, `copysign`, `pi`：来自 `mathutils` 和 `math` 模块，用于数学计算。
* `v.co`: 表示某个顶点的位置坐标。

#用途简述：

这段代码用于对选中的网格顶点进行处理，执行如下操作：

1. 获取选中顶点的位置半径 `r`。
2. 按平面 (1, 0, 0) 对 mesh 的上半部分进行切割。
3. 将切割结果的边和顶点进行拆分处理。
4. 执行一个展开变换（"unfurl"），把每个顶点的坐标从原始的 3D 空间变换成某种极坐标形式，使其围绕一个中心以角度 x 半径的方式重新布局。

#总结：

语言是 Python，但它依赖于 **Blender 的 Python API**（尤其是 `bpy` 和 `bmesh` 模块），因此只能在 Blender 的脚本编辑器或 Python 控制台中运行。
