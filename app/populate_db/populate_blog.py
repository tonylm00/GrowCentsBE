from app.models import BlogPost, db


def init_db_data():
    # Controlla se il database è già popolato
    if BlogPost.query.first() is None:
        posts = [
            BlogPost(title="Budgeting 101: Mastering the Art of Financial Management for Beginners",
                     content="Budgeting is a fundamental skill that everyone should master, regardless of their "
                             "financial goals. Whether you're saving for a dream vacation, planning for a major "
                             "purchase, or just aiming for a stress-free financial future, understanding how to "
                             "create and stick to a budget is the key to success. In this beginner's guide, "
                             "we'll explore the basics of budgeting, emphasizing the importance of distinguishing "
                             "between needs and wants in the realm of expenses.\nUnderstanding the Basics: What is "
                             "Budgeting?\nAt its core, budgeting is the process of creating a plan to manage your "
                             "money. It involves tracking your income, understanding your expenses, and ensuring that "
                             "your spending aligns with your financial goals. A budget acts as a roadmap, guiding you "
                             "toward your objectives and helping you make informed financial "
                             "decisions.\nDifferentiating Between Needs and Wants: A Crucial Distinction\nOne of the "
                             "fundamental principles of effective budgeting is distinguishing between needs and "
                             "wants. Needs are essential for survival and include items such as housing, food, "
                             "clothing, and healthcare. Wants, on the other hand, are things that enhance our lives "
                             "but are not necessary for survival, such as dining out, entertainment, and luxury "
                             "items."),

            BlogPost(title="The Importance of Regular Savings: Building Financial Security for Beginners",
                     content="Saving money is a crucial aspect of financial stability, providing a safety net for "
                             "unexpected expenses and securing a comfortable future. For beginners, understanding "
                             "the significance of regular savings and learning techniques to cut unnecessary expenses "
                             "can pave the way for a secure financial future. In this article, we will explore the "
                             "importance of saving regularly, strategies to save money, and how cutting frivolous "
                             "expenses can make a significant difference."),
        ]

        db.session.bulk_save_objects(posts)
        db.session.commit()
