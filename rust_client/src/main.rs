use api_example_poe_api::apis::configuration::Configuration;
use api_example_poe_api::apis::default_api;
use api_example_poe_api::models;

#[tokio::main]
async fn main() {
    let conf = Configuration {
        base_path: "http://127.0.0.1:7000".to_string(),
        ..Default::default()
    };
    let model = models::EnumModel {
        var: models::Dir::Variant999,
    };

    let resp = default_api::enum_io_enum_enum_io_post(&conf, model)
        .await
        .unwrap();
    dbg!(&resp);

    // let resp = default_api::text_pure_text_get(&conf).await.unwrap();
    // dbg!(&resp);
}
