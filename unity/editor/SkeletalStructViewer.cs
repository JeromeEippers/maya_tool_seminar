using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(SkeletalStructure), true)]
public class SkeletalStructViewer : Editor
{
    public override void OnInspectorGUI(){
        GUILayout.Label("Manage the drawing of the skeletal structure in the viewport");
    }

    private void DrawChildren(Transform start){
        var arrowHead = new Vector3[3];
        var arrowLine = new Vector3[2];

        for(int i=0; i < start.childCount; i++){
            var end = start.GetChild(i);
            
            var forward = (end.position - start.position).normalized;
            var right = Vector3.Cross(Camera.current.transform.forward, forward).normalized;
            var size = HandleUtility.GetHandleSize(end.position);
            var width = size * 0.1f;
            var height = size * 0.3f;

            arrowHead[0] = end.position;
            arrowHead[1] = end.position - forward * height + right*width;
            arrowHead[2] = end.position - forward * height - right*width;

            arrowLine[0] = start.position;
            arrowLine[1] = end.position - forward * height;

            Handles.color = Color.red;
            Handles.DrawAAPolyLine(arrowLine);
            Handles.DrawAAConvexPolygon(arrowHead);

            DrawChildren(end);
        }
    }
    public void OnSceneGUI(){
        SkeletalStructure t = target as SkeletalStructure;
        DrawChildren(t.transform);
    }
}
