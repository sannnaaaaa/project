def recommend_crop(soil_type):

    crop_data = {

        "Black Soil": [
            "Cotton",
            "Sugarcane",
            "Soybean"
        ],

        "Red Soil": [
            "Groundnut",
            "Millets",
            "Pulses"
        ],

        "Sandy Soil": [
            "Watermelon",
            "Groundnut",
            "Coconut"
        ],

        "Loamy Soil": [
            "Wheat",
            "Rice",
            "Vegetables"
        ]
    }

    return crop_data.get(soil_type, ["No crops found"])
