using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(Hooks), false)]
public class HooksEditor : Editor
{
    public void OnSceneGUI(){
        var t = target as Hooks;
        var trs = t.gameObject.transform;

        foreach(var hook in t.hooks){
            var position = trs.TransformPoint(hook.trs.pos);
            var quaternion = trs.rotation * hook.trs.quat;
            quaternion.Normalize();

            GUIStyle style = new GUIStyle();
            style.normal.textColor = Color.blue;
            Handles.Label(position, hook.name, style);

            EditorGUI.BeginChangeCheck();

            if (Tools.current == Tool.Move){
                position = Handles.PositionHandle(position, quaternion);
            }
            if (Tools.current == Tool.Rotate){
                quaternion = Handles.RotationHandle(quaternion, position);
            }

            if (EditorGUI.EndChangeCheck()){
                if (Tools.current == Tool.Move){
                    hook.trs.pos = trs.InverseTransformPoint(position);
                }
                else
                    hook.trs.quat = trs.worldToLocalMatrix.rotation * quaternion;
            }

        }
    }
}
