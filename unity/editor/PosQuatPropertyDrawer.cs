using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

[CustomPropertyDrawer(typeof(PosQuat))]
public class PosQuatPropertyDrawer : PropertyDrawer
{
    public override void OnGUI(Rect position, SerializedProperty property, GUIContent label){
        EditorGUI.BeginProperty(position, label, property);
        var pos_property = property.FindPropertyRelative("pos");
        var quat_property = property.FindPropertyRelative("quat");

        var posRect = new Rect(position.x, position.y, position.width, 20);
        var quatRect = new Rect(position.x, position.y + 20, position.width, 20);

        EditorGUI.BeginChangeCheck();

        var posValue = EditorGUI.Vector3Field(posRect, "Pos", pos_property.vector3Value);
        var quatValue = EditorGUI.Vector3Field(quatRect, "Rot", quat_property.quaternionValue.eulerAngles);

        if(EditorGUI.EndChangeCheck()){
            pos_property.vector3Value = posValue;
            quat_property.quaternionValue = Quaternion.Euler(quatValue);
        }


        EditorGUI.EndProperty();
    }

    public override float GetPropertyHeight(SerializedProperty property, GUIContent label)
    {
        return 40;
    }
}
