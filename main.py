import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def generate_caption(image_path):
    """
    Generate a caption for the given image using a pre-trained BLIP model.
    Args:
        image_path (str): Path to the input image.
    Returns:
        str: Generated caption for the image.
    """
    # Load the BLIP processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # Generate the caption
    with torch.no_grad():
        output_ids = model.generate(**inputs)
        caption = processor.decode(output_ids[0], skip_special_tokens=True)

    return caption

# Test the function (Optional for standalone execution)
if __name__ == "__main__":
    test_image = "images/example.jpg"  # Update the path to an existing image in your project
    print("Generating caption...")
    caption = generate_caption(test_image)
    print(f"Caption: {caption}")
