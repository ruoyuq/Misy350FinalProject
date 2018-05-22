from flask_script import Manager
from bookstore import app, db, Author, Book

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    jane = Author(name='Jane Austen', intro='Jane Austen was an English novelist known primarily for her six major novels, got the British landed gentry at the end of the 18th century.')
    yh = Author(name='Yu Hua', intro='Yu Hua is a Chinese author, born April 3, 1960 in Hangzhou, Zhejiang province.')
    scott = Author(name='F. Scott Fitzgerald', intro='an American novelist and short story writer, whose works illustrate the Jazz Age')
    book1=Book(name='Pride and Prejudice', year='1813', author_id=1, summary='A romance novel by Jane Austen, first published in 1813. The story charts the emotional development of the protagonist, Elizabeth Bennet, who learns the error of making hasty judgments and comes to appreciate the difference between the superficial and the essential. The comedy of the writing lies in the depiction of manners, education, marriage, and money in the British Regency.')
    book2=Book(name='To Live', year='1993', author_id=2, summary='To Live is one of the most representative work by Yu Hua. The story begins with the narrator traveling through the countryside to collect folk songs and local legends and starting to hear a old peasant talking about his experiences, which encompass many significant historical events in China including the Great Leap Forward, Three-anti and Five-anti Campaigns and Cultural Revolution. ')
    book5=Book(name='The Great Gatsby', year='1922', author_id=3, summary='The Great Gatsby is a 1925 novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the fictional town of West Egg on prosperous Long Island in the summer of 1922. ')

    db.session.add(yh)
    db.session.add(jk)
    db.session.add(scott)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book5)


    db.session.commit()


if __name__ == "__main__":
    manager.run()
