您说：
import bpy
import bmesh
from mathutils import Vector
from math import copysign, pi

context = bpy.context

ob = context.object
me = ob.data

bm = bmesh.from_edit_mesh(me)
#bm.from_mesh(me)

v_r = bm.select_history.active
r = v_r.co.xy.length

assert(isinstance(v_r, bmesh.types.BMVert), "Select a Vert")
cut = bmesh.ops.bisect_plane(
        bm,
        geom=[f for f in bm.faces if all(v.co.y > 0 for v in f.verts)] + [e for e in bm.edges if all(v.co.y > 0 for v in e.verts)] + [v for v in bm.verts if v.co > 0],
        plane_no=(1, 0, 0),
        )["geom_cut"]
    
for g in cut:
    g.select = True


bmesh.ops.split_edges(
        bm,
        edges=[e for e in cut if isinstance(e, bmesh.types.BMEdge)],
        verts=[v for v in cut if isinstance(v, bmesh.types.BMVert)],
        use_verts=True
        )

    
# now "unfurl"

up = Vector((0, -1))
for v in bm.verts:
    co = v.co.copy()
    angle = -up.angle_signed(v.co.xy)
    if 1 + up.dot(v.co.xy.normalized()) < 1e-4:
        # meridian 
        fv = sum((f.calc_center_median().x 
            for f in v.link_faces)
                 ) / len(v.link_faces)
        v.select_set(True)
        angle = copysign(angle, fv)
    v.co.z= co.z
    v.co.y = -co.xy.length + r
    v.co.x = angle * r

  
bmesh.update_edit_mesh(me)