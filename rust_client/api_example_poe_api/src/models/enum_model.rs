/*
 * FastAPI
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EnumModel {
    #[serde(rename = "var")]
    pub var: crate::models::Dir,
}

impl EnumModel {
    pub fn new(var: crate::models::Dir) -> EnumModel {
        EnumModel {
            var,
        }
    }
}


