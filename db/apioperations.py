from db import queries
from db.operations import Operations

op = Operations()
#
# op.getop()
#

res = op.queryexec(queries.query)
# print(res)
#
# op.gen_sql(queries.query2)

res_json_vals=op.generate_Json(res)
# print(res_json_vals)

ids_post = op.indi_json(res_json_vals)
print(ids_post)


op.get_pros_by_id(ids_post)

