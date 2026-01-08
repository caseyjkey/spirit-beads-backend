#!/usr/bin/env python3
"""
Create test images for import_lighters command
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image(filename, text, color=(100, 150, 200)):
    """Create a simple test image with text"""
    # Create a simple 200x200 image
    img = Image.new('RGB', (200, 200), color)
    draw = ImageDraw.Draw(img)
    
    # Add text to identify the image
    try:
        # Try to use a default font
        font = ImageFont.load_default()
    except:
        font = None
    
    # Draw text in the center
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (200 - text_width) // 2
    y = (200 - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save as PNG
    img.save(filename, 'PNG')
    print(f"Created: {filename}")

def main():
    # Create test directory
    test_dir = Path("/tmp/test_lighters")
    test_dir.mkdir(exist_ok=True)
    
    # Generate 50 diverse test cases
    import random
    
    names = [
        "Feather-Sun", "Mountain-View", "Ocean-Wave", "Desert-Rose", "Double-Eagle",
        "Spirit-Wolf", "Moon-Dance", "Star-Fire", "Wind-Whisper", "River-Stone",
        "Forest-Dream", "Thunder-Bolt", "Lightning-Strike", "Crystal-Heart", "Eagle-Eye",
        "Wolf-Spirit", "Bear-Claw", "Hawk-Flight", "Snake-Charm", "Lion-Heart",
        "Dragon-Breath", "Phoenix-Rise", "Tiger-Stripe", "Leopard-Spot", "Cheetah-Run",
        "Panther-Prowl", "Jaguar-Spirit", "Cobra-Strike", "Viper-Fang", "Python-Coil",
        "Eagle-Wing", "Hawk-Talon", "Owl-Wisdom", "Raven-Cry", "Crow-Flight",
        "Sparrow-Song", "Robin-Red", "Blue-Jay", "Cardinal-Song", "Finch-Dance",
        "Swallow-Flight", "Swan-Grace", "Goose-Flight", "Duck-Paddle", "Heron-Stand",
        "Egret-White", "Stork-Flight", "Crane-Dance", "Flamingo-Pink", "Pelican-Dive"
    ]
    
    categories = [
        "Infinite-Path", "Earths-Hue", "Traditional-Rhythms", "Ancestral-Motifs", "Spirit-Path",
        "Cosmic-Dance", "Sacred-Geometry", "Ancient-Wisdom", "Mystic-Journey", "Divine-Light"
    ]
    
    test_cases = []
    for i in range(50):
        name = names[i % len(names)]
        category = random.choice(categories)
        price = random.randint(35, 85)
        
        # Generate random color
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        
        # Always create primary image
        test_cases.append((f"{name}_{category}_{price}-1.png", f"{name}\nPrimary", color))
        
        # 70% chance of having secondary image
        if random.random() < 0.7:
            # Complementary color for secondary
            secondary_color = (255 - color[0], 255 - color[1], 255 - color[2])
            test_cases.append((f"{name}_{category}_{price}-2.png", f"{name}\nSecondary", secondary_color))
    
    for filename, text, color in test_cases:
        filepath = test_dir / filename
        create_test_image(filepath, text, color)
    
    print(f"\nCreated {len(test_cases)} test images in {test_dir}")
    print("You can now test the import with:")
    print(f"python manage.py import_lighters {test_dir} --dry-run")

if __name__ == "__main__":
    main()
