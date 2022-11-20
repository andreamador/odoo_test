# odoo_test


Erro:
Odoo Server Error

Traceback (most recent call last):
  File "/odoo/odoo/odoo/tools/convert.py", line 677, in _tag_root
    f(rec)
  File "/odoo/odoo/odoo/tools/convert.py", line 580, in _tag_record
    record = model._load_records([data], self.mode == 'update')
  File "/odoo/odoo/odoo/models.py", line 4236, in _load_records
    records = self._load_records_create([data['values'] for data in to_create])
  File "/odoo/odoo/odoo/models.py", line 4152, in _load_records_create
    return self.create(values)
  File "<decorator-gen-43>", line 2, in create
  File "/odoo/odoo/odoo/api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 482, in create
    return super(View, self).create(vals_list)
  File "<decorator-gen-65>", line 2, in create
  File "/odoo/odoo/odoo/api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "/odoo/odoo/odoo/addons/base/models/ir_fields.py", line 534, in create
    recs = super().create(vals_list)
  File "<decorator-gen-13>", line 2, in create
  File "/odoo/odoo/odoo/api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "/odoo/odoo/odoo/models.py", line 3909, in create
    fields[0].determine_inverse(batch_recs)
  File "/odoo/odoo/odoo/fields.py", line 1187, in determine_inverse
    getattr(records, self.inverse)()
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 300, in _inverse_arch
    view.write(data)
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 500, in write
    res = super(View, self).write(self._compute_defaults(vals))
  File "/odoo/odoo/odoo/models.py", line 3693, in write
    real_recs._validate_fields(vals, inverse_fields)
  File "/odoo/odoo/odoo/models.py", line 1266, in _validate_fields
    check(self)
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 408, in _check_xml
    raise ValidationError(_(
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 385, in _check_xml
    view_def = view.read_combined(['arch'])
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 809, in read_combined
    arch = root.apply_view_inheritance(arch_tree, self.model)
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 750, in apply_view_inheritance
    return self._apply_view_inheritance(source, inherit_tree)
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 758, in _apply_view_inheritance
    source = view.apply_inheritance_specs(source, arch_tree)
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 735, in apply_inheritance_specs
    self.handle_view_error(str(e))
  File "/odoo/odoo/odoo/addons/base/models/ir_ui_view.py", line 673, in handle_view_error
    raise ValueError(formatted_message).with_traceback(from_traceback) from from_exception
odoo.exceptions.ValidationError: Erro ao validar a visualização:

Elemento '<field name="document_type_id">' não pode ser localizado na vista principal

View name: custom_account.invoice.form
Error context:
 view: ir.ui.view(2091,)
 xmlid: invoice_form_custom
 view.model: account.move
 view.parent: ir.ui.view(611,)
 file: /odoo/odoo/addons-extra/custom_account/views/account_invoice_view.xml


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/odoo/odoo/odoo/addons/base/models/ir_http.py", line 237, in _dispatch
    result = request.dispatch()
  File "/odoo/odoo/odoo/http.py", line 683, in dispatch
    result = self._call_function(**self.params)
  File "/odoo/odoo/odoo/http.py", line 359, in _call_function
    return checked_call(self.db, *args, **kwargs)
  File "/odoo/odoo/odoo/service/model.py", line 94, in wrapper
    return f(dbname, *args, **kwargs)
  File "/odoo/odoo/odoo/http.py", line 347, in checked_call
    result = self.endpoint(*a, **kw)
  File "/odoo/odoo/odoo/http.py", line 912, in __call__
    return self.method(*args, **kw)
  File "/odoo/odoo/odoo/http.py", line 531, in response_wrap
    response = f(*args, **kw)
  File "/odoo/odoo/addons/web/controllers/main.py", line 1393, in call_button
    action = self._call_kw(model, method, args, kwargs)
  File "/odoo/odoo/addons/web/controllers/main.py", line 1381, in _call_kw
    return call_kw(request.env[model], method, args, kwargs)
  File "/odoo/odoo/odoo/api.py", line 399, in call_kw
    result = _call_kw_multi(method, model, args, kwargs)
  File "/odoo/odoo/odoo/api.py", line 386, in _call_kw_multi
    result = method(recs, *args, **kwargs)
  File "<decorator-gen-78>", line 2, in button_immediate_upgrade
  File "/odoo/odoo/odoo/addons/base/models/ir_module.py", line 74, in check_and_log
    return method(self, *args, **kwargs)
  File "/odoo/odoo/odoo/addons/base/models/ir_module.py", line 654, in button_immediate_upgrade
    return self._button_immediate_function(type(self).button_upgrade)
  File "/odoo/odoo/odoo/addons/base/models/ir_module.py", line 593, in _button_immediate_function
    modules.registry.Registry.new(self._cr.dbname, update_module=True)
  File "/odoo/odoo/odoo/modules/registry.py", line 89, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/odoo/odoo/odoo/modules/loading.py", line 455, in load_modules
    processed_modules += load_marked_modules(cr, graph,
  File "/odoo/odoo/odoo/modules/loading.py", line 347, in load_marked_modules
    loaded, processed = load_module_graph(
  File "/odoo/odoo/odoo/modules/loading.py", line 222, in load_module_graph
    load_data(cr, idref, mode, kind='data', package=package)
  File "/odoo/odoo/odoo/modules/loading.py", line 69, in load_data
    tools.convert_file(cr, package.name, filename, idref, mode, noupdate, kind)
  File "/odoo/odoo/odoo/tools/convert.py", line 733, in convert_file
    convert_xml_import(cr, module, fp, idref, mode, noupdate)
  File "/odoo/odoo/odoo/tools/convert.py", line 799, in convert_xml_import
    obj.parse(doc.getroot())
  File "/odoo/odoo/odoo/tools/convert.py", line 719, in parse
    self._tag_root(de)
  File "/odoo/odoo/odoo/tools/convert.py", line 681, in _tag_root
    raise ParseError('while parsing %s:%s, near\n%s' % (
Exception

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/odoo/odoo/odoo/http.py", line 639, in _handle_exception
    return super(JsonRequest, self)._handle_exception(exception)
  File "/odoo/odoo/odoo/http.py", line 315, in _handle_exception
    raise exception.with_traceback(None) from new_cause
odoo.tools.convert.ParseError: while parsing /odoo/odoo/addons-extra/custom_account/views/account_invoice_view.xml:5, near
<record id="invoice_form_custom" model="ir.ui.view">
        <field name="name">custom_account.invoice.form</field>
        <field name="model">account.move</field>
        <field name="inherit_id" ref="account.view_move_form"/>
        <field name="arch" type="xml">
        
            <field name="document_type_id" position="before">
                <p> oLA </p>
            </field>

        </field>
    </record>