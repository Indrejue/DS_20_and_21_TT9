import pandas as pd
import numpy as np
from joblib import load

flavors = ['earthy', 'tree_fruit', 'pine', 'vanilla', 'sweet', 'chestnut', 'apricot', 'apple', 
            'skunk', 'grape', 'diesel', 'lime', 'honey', 'pungent', 'violet', 'menthol', 'chemical', 'cheese',
            'mango', 'orange', 'lavender', 'plum', 'citrus', 'tar', 'spicy_herbal', 'minty', 'butter', 
            'peach', 'nutty', 'mint', 'berry', 'ammonia', 'pear', 'rose', 'pineapple', 'blue_cheese', 'tea', 
            'flowery', 'strawberry', 'grapefruit', 'sage', 'blueberry', 'woody', 'tobacco', 'tropical', 
            'pepper', 'coffee', 'lemon']

effects = ['giggly', 'paranoid', 'uplifted', 'aroused', 'horny', 'sleepy', 'talkative', 'hungry', 
            'tingly', 'energetic', 'relaxed', 'focused', 'dry_mouth', 'creative', 'euphoric', 'happy', 
            'anxious']

ailments = ['insomnia', 'lack_of_appetite', 'stress', 'nausea', 'pain', 'inflammation', 'depression', 
            'muscle_spasms']

categories = ['crumble', 'pre-roll', 'drink', 'bath', 'soup', 'spread', 'wax', 'vape_cartidge', 
            'snack', 'kief', 'candy', 'bubble_hash', 'vapes', 'pill', 'tincture', 'dressing', 'salt', 
            'chocolate', 'disposable_vape', 'oil', 'concentrate', 'rso', 'shatter', 'topical', 'edibles', 
            'flowers']

def predict_strain():
    """
    Determine and return strain
    """
    return 



