using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public struct PosQuat
{
    public Vector3 pos;
    public Quaternion quat;

    public static PosQuat identity{ get{
        return new PosQuat() {pos = Vector3.zero, quat=Quaternion.identity};
    }}

    
}
