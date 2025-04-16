import re
import spacy

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.nlp = spacy.load("en_core_web_sm")
        

    def count_words(self):
        word_list = self.title.split() + self.contents.split()
        return len(word_list)

    def reading_time(self, wpm):
        if self.count_words() == 0:
            return "No entries yet"
        if self.count_words()% wpm == 0:
            return (self.count_words()//wpm)
        else:
            return (self.count_words()//wpm) + 1
        

    def extract_phone_numbers(self):
        phone_pattern = r"(?:\+44|0)\d{10}"
        phone_matches = phone_matches = [(match.group(), match.start()) for match in re.finditer(phone_pattern, self.contents)]
        print(self.contents)
        print(phone_matches)
        doc = self.nlp(self.contents)
        name_entities = [(ent.text, ent.start_char) for ent in doc.ents if ent.label_ == "PERSON"]
        print(name_entities)
        contacts = []
        for phone, phone_pos in phone_matches:
            closest_name = None
            min_distance = float('inf')

            for name, name_pos in name_entities:
                if name_pos < phone_pos:  
                    distance = phone_pos - name_pos
                    if distance < min_distance:
                        closest_name = name
                        min_distance = distance

            contacts.append({
                "name": closest_name if closest_name else "Unknown",
                "phone": phone
            })

        return contacts