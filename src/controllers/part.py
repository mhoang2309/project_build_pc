from flask import Blueprint, make_response, request
from flask.views import MethodView
from src.models.part import Part
from src.controllers.check_token import token_required, is_admin
from src.controllers.database import db_build_pc
import json


parts_bp = Blueprint('parts_bp',__name__)    

class Parts(MethodView):
    @token_required
    @is_admin
    def get(self):       
        data=[]
        if request.args:
            try:
                name = request.args['name']
            except:
                 name = ''
            try:
                type = request.args['type']
            except:
                type = "%%"
            part = db_build_pc.query(Part).filter( Part.name.like("%{}%".format(name)), Part.type.like(type)).all()
            for i in part:
                s ={"name":i.name, "type":i.type, "price":float(i.price)}
                data.append(s)

        else:
            part = db_build_pc.query(Part).all()
            for i in part:
                s ={"name":i.name, "type":i.type, "price":float(i.price)}
                data.append(s)

        return json.dumps(data)
        
    
    
    @token_required
    @is_admin
    def post(self):
        name = request.json['name']
        type = request.json['type']
        price = request.json['price']
        set_part = Part(name=name, type=type, price=price)
        db_build_pc.add(set_part)
        db_build_pc.commit()
        return make_response({'message':'OK new part'}, 200)

   
    
class Part_(MethodView):
    @token_required
    @is_admin
    def put(self, part_id):
        name = request.json['name']
        type = request.json['type']
        price = request.json['price']
        part = Part.query.get(part_id)
        try:
            part.name = name
            part.type = type
            part.price = price
            db_build_pc.commit()
        except:
            return make_response({'message':'Update err'}, 401)
        return make_response({'message':'Update successful'}, 200)
    
    @token_required
    @is_admin
    def delete(self, part_id):
        if db_build_pc.query(Part).filter_by(id=part_id).first():
            db_build_pc.query(Part).filter_by(id=part_id).delete()
            db_build_pc.commit()
            return make_response({'message':'ok'}, 200)
        return make_response({'message':'Delete err'}, 404)

parts_view = Parts.as_view("parts_api")
parts_bp.add_url_rule("",view_func=parts_view, methods=['GET', 'POST'])

part_view = Part_.as_view("part_api")
parts_bp.add_url_rule("/<int:part_id>",view_func=part_view, methods=['DELETE', 'PUT'])



