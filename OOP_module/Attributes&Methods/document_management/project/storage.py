# import typing
# from document_management.project.category import Category
# from document_management.project.document import Document
# from document_management.project.topic import Topic
#

class Storage:
    categories = []
    topics = []
    documents = []

    def add_category(self, category):
        if category not in Storage.categories:
            Storage.categories.append(category)

    def add_topic(self, topic):
        if topic not in Storage.topics:
            Storage.topics.append(topic)

    def add_document(self, document):
        if document not in Storage.documents:
            Storage.documents.append(document)

    def edit_category(self, category_id, new_name):
        category_obj_list = [x for x in Storage.categories if x.id == category_id]
        if category_obj_list:
            category_obj = category_obj_list[0]
            category_obj.name = new_name
            return

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic_obj_list = [x for x in Storage.topics if x.id == topic_id]
        if topic_obj_list:
            topic_obj = topic_obj_list[0]
            topic_obj.topic = new_topic
            topic_obj.storage_folder = new_storage_folder
            return

    def edit_document(self, document_id: int, new_file_name: str):
        document_obj_list = [x for x in Storage.documents if x.id == document_id]
        if document_obj_list:
            document_obj = document_obj_list[0]
            document_obj.file_name = new_file_name
            return

    def delete_category(self, category_id):
        category_obj_list = [x for x in Storage.categories if x.id == category_id]
        if category_obj_list:
            category_obj = category_obj_list[0]
            Storage.categories.remove(category_obj)
            return

    def delete_topic(self, topic_id):
        topic_obj_list = [x for x in Storage.topics if x.id == topic_id]
        if topic_obj_list:
            topic_obj = topic_obj_list[0]
            Storage.topics.remove(topic_obj)
            return

    def delete_document(self, document_id):
        Storage.documents = [x for x in Storage.documents if x.id != document_id]
        return

    def get_document(seld, document_id):
        return [x for x in Storage.documents if x.id == document_id]

    def __repr__(self):
        for document in Storage.documents:
            return f"{document}"


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
