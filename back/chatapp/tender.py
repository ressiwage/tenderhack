from flask import (
    Blueprint, request, current_app, jsonify, abort, Response, send_file
)
from core import Tender, Document
from db import engine, db_session, Base
from utils import create_dummy_objects

bp = Blueprint('tender', __name__, url_prefix='/api_v0')


@bp.route('/tenders', methods=['GET'])
def tenders():
    res = Tender.query.all()
    return jsonify([x.to_dict() for x in res])


@bp.route('/documents', methods=['GET'])
def documents():
    res = Tender.query.all()
    raise NotImplementedError


@bp.route('/add-tender', methods=['POST'])
def add_tender():
    obj = Tender(description="wow", tender_number=123)
    db_session.add(obj)
    db_session.commit()
    return f"Added {obj}", 200


@bp.route('/add-document', methods=['GET'])
def add_document():
    obj = Document(document_name="TestDoc", tender_id=1, document_type=2)
    db_session.add(obj)
    db_session.commit()
    return f"Added {obj}", 200


@bp.route('/add-contract-clause', methods=['GET'])
def add_contract_clause():
    obj = Document(document_name="TestDoc", tender_id=1, document_type=2)
    db_session.add(obj)
    db_session.commit()
    return f"Added {obj}", 200


@bp.route('/delete-tender', methods=['DELETE'])
def delete_tender():
    obj = Tender.query.filter_by(id=1).first()
    db_session.query(Tender).filter(Tender.id == 1).delete()
    db_session.commit()
    return f"Deleted {obj}", 200


@bp.route('/populate-db', methods=['GET'])
def populate_db():
    create_dummy_objects()
    return "OK", 200


@bp.route('/demo-query-foreign-key', methods=['GET'])
def demo_query_foreign_key():
    # Получаем объект по id
    test_tender = Tender.query.get(1)
    print(test_tender)
    # Получаем список всех документов, которые относятся к этому тендеру
    docs = test_tender.tender_documents
    print(docs)
    # Получаем тендер, к которому привязан данный документ
    tender = docs[0].tender
    print(tender)
    return jsonify([doc.to_dict() for doc in docs]), 200
