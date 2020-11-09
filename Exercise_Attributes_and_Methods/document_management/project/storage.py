# from document_management.project.category import Category
# from document_management.project.topic import Topic
# from document_management.project.document import Document
# from typing import List


class Storage:
    def __init__(self):
        self.categories: list = []
        self.topics = []
        self.documents = []

    def add_category(self, category) -> None:
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic) -> None:
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document) -> None:
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        categories_ids = list(map(lambda c: c.id, self.categories))
        if category_id in categories_ids:
            self.categories[categories_ids.index(category_id)].edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topics_ids = list(map(lambda t: t.id, self.topics))
        if topic_id in topics_ids:
            self.topics[topics_ids.index(topic_id)].edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        documents_ids = list(map(lambda d: d.id, self.documents))
        if document_id in documents_ids:
            self.documents[documents_ids.index(document_id)].edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        categories_ids = list(map(lambda c: c.id, self.categories))
        if category_id in categories_ids:
            self.categories.pop(categories_ids.index(category_id))

    def delete_topic(self, topic_id: int) -> None:
        topics_ids = list(map(lambda t: t.id, self.topics))
        if topic_id in topics_ids:
            self.topics.pop(topics_ids.index(topic_id))

    def delete_document(self, document_id: int) -> None:
        documents_ids = list(map(lambda d: d.id, self.documents))
        if document_id in documents_ids:
            self.documents.pop(documents_ids.index(document_id))

    def get_document(self, document_id: int):
        documents_ids = list(map(lambda d: d.id, self.documents))
        if document_id in documents_ids:
            return self.documents[documents_ids.index(document_id)]

    def __repr__(self):
        return "\n".join(repr(d) for d in self.documents)


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
