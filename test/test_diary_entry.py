from lib.diary_entry import DiaryEntry

def test_stores_title_and_contents():
    entry = DiaryEntry("How I spent summer", 
                       "It was fairly boring few weeks")
    
    assert entry.title == "How I spent summer"
    assert entry.contents == "It was fairly boring few weeks"

def test_count_words_returns_correct_number_and_format():
    entry = DiaryEntry("How I spent summer?", 
                       "It was fairly boring few weeks!")
    result = entry.count_words()

    assert isinstance(result, int)
    assert result == 10

def test_returns_correct_min_estimation():
    entry = DiaryEntry("How I spent summer", 
                       "It was fairly boring few weeks!")
    result = entry.reading_time(2)

    assert result == 5

    result = entry.reading_time(3)

    assert result == 4

def test_extract_phone_catches_phones_without_names():
    entry = DiaryEntry("How I spent summer", 
            "I met a friend and she shared her number with me 07772222222!")
    result = entry.extract_phone_numbers()

    assert result == [{"name" : "Unknown", "phone" : "07772222222"}]

def test_extract_phone_catches_both_name_and_number():
    entry = DiaryEntry("How I spent summer", 
            "I met Alicia and she shared her number with me 07772222222!")
    result = entry.extract_phone_numbers()

    assert result == [{"name" : "Alicia", "phone" : "07772222222"}]

def test_extract_phone_correctly_assumes_name_among_multiple_capitalized_words():
    entry = DiaryEntry("How I spent summer", 
            "I met Alicia in London while waiting for my coffee at Starbucks \
            and she shared her number with me 07772222222!")
    result = entry.extract_phone_numbers()

    assert result == [{"name" : "Alicia", "phone" : "07772222222"}]