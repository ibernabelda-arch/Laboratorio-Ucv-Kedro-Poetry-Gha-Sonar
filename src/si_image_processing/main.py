from si_image_processing.pipelines.image_processing.nodes import process_image

input_image = "data/01_raw/marte.jpg"
output_image = "data/03_primary/marte_processed.jpg"

process_image(input_image, output_image)

print("Imagen procesada correctamente")