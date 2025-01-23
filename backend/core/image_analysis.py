# image_analysis.py
from pydantic import BaseModel
import requests
from PIL import Image
import io

class ImageAnalysis(BaseModel):
    setting: str
    characters: list[str]
    mood: str
    objects: list[str]
    potential_conflicts: list[str]

class MultimodalAnalyzer:
    def __init__(self, model="llava"):
        self.model = model
        
    def analyze(self, image_path):
        if self.model == "llava":
            return self._analyze_with_llava(image_path)
        else:
            return self._analyze_with_gpt4v(image_path)

    def _analyze_with_llava(self, image):
        prompt = """Describe this image in JSON format with: 
        setting, characters, mood, objects, and potential_conflicts"""
        
        # Implementation for Ollama LLaVA API call
        response = ollama.generate(
            model="llava",
            prompt=prompt,
            images=[image],
            format="json"
        )
        return ImageAnalysis.parse_raw(response.text)