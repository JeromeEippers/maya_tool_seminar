using UnityEngine;
using UnityEditor;


public class MyTextureImporter : AssetPostprocessor
{
    void OnPreprocessTexture()
    {
        if (assetPath.Contains("_Normal"))
        {
            TextureImporter textureImporter  = (TextureImporter)assetImporter;
            textureImporter.textureType = TextureImporterType.NormalMap;
        }

        if(assetPath.Contains("_Normal")==false && assetPath.Contains("_BaseColor")==false){
            TextureImporter textureImporter  = (TextureImporter)assetImporter;
            textureImporter.textureType = TextureImporterType.Default;
            textureImporter.sRGBTexture = false;
        }
    }
}
