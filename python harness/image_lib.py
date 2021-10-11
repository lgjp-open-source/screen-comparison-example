import io
import cv2
from difflib import SequenceMatcher
from google.cloud import vision

class CustomParagraph:
  def __init__(self, bound, value):
    self.bound = bound
    self.value = value

def get_paragraph_value(paragraph):
    value =''
    for word in paragraph.words:
        for symbol in word.symbols:
            value += symbol.text
    return value

def get_word_value(word):
    value =''
    for symbol in word.symbols:
        value += symbol.text
    return value

def get_paragraph_texts_and_bounds(image_file):
    """Returns paragraph bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                value = get_paragraph_value(paragraph)
                bounds.append(CustomParagraph(paragraph.bounding_box, value))
    return bounds

def get_word_texts_and_bounds(image_file):
    """Returns word bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    value = get_word_value(word)
                    bounds.append(CustomParagraph(word.bounding_box, value))
    return bounds

def convert_to_grayscale(input, output):
    image = cv2.imread(input)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output, gray)

def get_paragraph_in_target_array(base, target_array, match_percent):
    for paragraph in target_array:
        if(match_percent == 100):
            if (base.value == paragraph.value):
                target_array.remove(paragraph)
                return paragraph
        else:
            #print(base.value + " - " + paragraph.value + " :" + str(SequenceMatcher(None, base.value, paragraph.value).ratio()))
            if (SequenceMatcher(None, base.value, paragraph.value).ratio() >= match_percent/100):
                #print("------ " + base.value + " - " + paragraph.value + " :" + str(SequenceMatcher(None, base.value, paragraph.value).ratio()))
                target_array.remove(paragraph)
                return paragraph
    return None

def get_background_color(data, left, right, row, text_color):
    pixels = []
    for col in range(left,right):
        if (text_color != data[row, col]):
            pixels.append(data[row, col])
    if (len(pixels) > 0):
        return max(pixels, key = pixels.count)
    return text_color

def clear_text(data, bound, indent, text_color):
    right = 0
    bottom = 0
    left = data.shape[1]    #width
    top = data.shape[0]     #height
    for vertices in bound.vertices:
        if (vertices.x < left):
            left = vertices.x
        if (vertices.y < top):
            top = vertices.y
        if (right <  vertices.x):
            right = vertices.x
        if (bottom <  vertices.y):
            bottom = vertices.y

    # Replace bound with background color
    left = left - indent if left > indent else 0
    right = right + indent if right + indent < data.shape[1] else data.shape[1]
    top = top -indent if top > indent else 0
    bottom = bottom + indent if bottom + indent < data.shape[0] else data.shape[0]

    for row in range(top,bottom):
        bg = get_background_color(data, left, right, row, text_color)
        for col in range(left,right):
            data[row, col] = bg

def replace_identical_paragraph_pictures(input_base, input_target, output_base, output_target, indent, text_color, match_percent):

    # Get paragraph values in grayscale file
    base_paragraphs = get_paragraph_texts_and_bounds(input_base)
    target_paragraphs = get_paragraph_texts_and_bounds(input_target)

    # OpenCV data file for grayscale images
    base_image_data = cv2.imread(input_base, cv2.IMREAD_GRAYSCALE)
    target_image_data = cv2.imread(input_target, cv2.IMREAD_GRAYSCALE)

    for paragraph in base_paragraphs:
        target_paragraph = get_paragraph_in_target_array(paragraph, target_paragraphs, match_percent)
        if (target_paragraph != None):            
            clear_text(base_image_data, paragraph.bound, indent, text_color)
            clear_text(target_image_data, target_paragraph.bound, indent, text_color)
    
    # Save images
    cv2.imwrite(output_base, base_image_data)
    cv2.imwrite(output_target, target_image_data)

def clear_word(word, input):
    words = get_word_texts_and_bounds(input)
    # OpenCV data file for grayscale images
    image = cv2.imread(input, cv2.IMREAD_GRAYSCALE)
    for text in words:
        if (text.value == word):
            clear_text(image, text.bound, 3, 0)
    
    # Overwrite images
    cv2.imwrite(input, image)