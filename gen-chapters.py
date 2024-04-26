import argparse
import xml.dom.minidom

def create_chapter_xml(chapter_timings, use_names):
    doc = xml.dom.minidom.Document()

    chapters = doc.createElement('Chapters')
    doc.appendChild(chapters)

    edition_entry = doc.createElement('EditionEntry')
    chapters.appendChild(edition_entry)

    edition_uid = doc.createElement('EditionUID')
    edition_uid.appendChild(doc.createTextNode('1886527968354451490'))
    edition_entry.appendChild(edition_uid)

    chapter_uid_counter = 1

    for index, timing in enumerate(chapter_timings, start=1):
        chapter_atom = doc.createElement('ChapterAtom')
        edition_entry.appendChild(chapter_atom)

        chapter_time_start = doc.createElement('ChapterTimeStart')
        chapter_time_start.appendChild(doc.createTextNode(timing[0]))
        chapter_atom.appendChild(chapter_time_start)

        chapter_flag_hidden = doc.createElement('ChapterFlagHidden')
        chapter_flag_hidden.appendChild(doc.createTextNode('0'))
        chapter_atom.appendChild(chapter_flag_hidden)

        chapter_flag_enabled = doc.createElement('ChapterFlagEnabled')
        chapter_flag_enabled.appendChild(doc.createTextNode('1'))
        chapter_atom.appendChild(chapter_flag_enabled)

        chapter_display = doc.createElement('ChapterDisplay')
        chapter_atom.appendChild(chapter_display)

        if use_names and len(timing) > 1:
            chapter_string = doc.createElement('ChapterString')
            chapter_string.appendChild(doc.createTextNode(timing[1]))
            chapter_display.appendChild(chapter_string)
        else:
            chapter_string = doc.createElement('ChapterString')
            chapter_string.appendChild(doc.createTextNode(f'Chapter {str(index).zfill(2)}'))
            chapter_display.appendChild(chapter_string)

        chapter_language = doc.createElement('ChapterLanguage')
        chapter_language.appendChild(doc.createTextNode('en'))
        chapter_display.appendChild(chapter_language)

        chap_language_ietf = doc.createElement('ChapLanguageIETF')
        chap_language_ietf.appendChild(doc.createTextNode('en'))
        chapter_display.appendChild(chap_language_ietf)

        chapter_uid = doc.createElement('ChapterUID')
        chapter_uid.appendChild(doc.createTextNode(str(chapter_uid_counter)))
        chapter_atom.appendChild(chapter_uid)

        chapter_uid_counter += 1

    return doc.toprettyxml(indent='')

def write_chapter_metadata(filename, chapters):
    with open(filename, 'w') as file:
        file.write(chapters)

def read_timings_from_file(file_path):
    timings = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Splitting on the first occurrence of ' : ' to handle names with ':' inside
                timing = line.split(" : ", 1)
                timings.append(timing)
    return timings

def main():
    parser = argparse.ArgumentParser(description='Create chapter metadata for MKV movies')
    parser.add_argument('filename', help='Output filename for the chapter metadata')
    parser.add_argument('input_file', help='Path to the input text file containing chapter timings')
    parser.add_argument('-names', action='store_true', help='Use provided chapter names')
    args = parser.parse_args()

    chapter_timings = read_timings_from_file(args.input_file)
    chapters = create_chapter_xml(chapter_timings, args.names)
    write_chapter_metadata(args.filename, chapters)

    print(f'Chapter metadata created successfully in "{args.filename}".')

if __name__ == '__main__':
    main()
