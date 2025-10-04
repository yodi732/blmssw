from .tool.func import *

# 개편 필요
async def login_find_email_check(tool):
    with get_db_connect() as conn:
        curs = conn.cursor()
        
        if flask.request.method == 'POST' or ('c_key' in flask.session and flask.session['c_key'] == 'email_pass'):
            re_set_list = ['c_id', 'c_pw', 'c_ans', 'c_que', 'c_key', 'c_type', 'c_email']

            ip = ip_check()
            
            input_key = flask.request.form.get('key', '')
            user_agent = flask.request.headers.get('User-Agent', '')
        
            if 'c_type' in flask.session and flask.session['c_type'] == 'pass_find' and flask.session['c_key'] == input_key:
                user_id = flask.session['c_id']
                user_pw = flask.session['c_key']
            
                curs.execute(db_change("update user_set set data = ? where name = 'pw' and id = ?"), [pw_encode(conn, user_pw), user_id])
                
                curs.execute(db_change('select data from user_set where name = "2fa" and id = ?'), [user_id])
                if curs.fetchall():
                    curs.execute(db_change("update user_set set data = '' where name = '2fa' and id = ?"), [user_id])
        
                for i in re_set_list:
                    flask.session.pop(i, None)
        
                curs.execute(db_change('select data from other where name = "reset_user_text"'))
                sql_d = curs.fetchall()
                b_text = (sql_d[0][0] + '<hr class="main_hr">') if sql_d and sql_d[0][0] != '' else ''
        
                return easy_minify(conn, flask.render_template(skin_check(conn),
                    imp = [get_lang(conn, 'reset_user_ok'), await wiki_set(), await wiki_custom(conn), wiki_css([0, 0])],
                    data = '' + \
                        b_text + \
                        get_lang(conn, 'id') + ' : ' + user_id + \
                        '<hr class="main_hr">' + \
                        get_lang(conn, 'password') + ' : ' + user_pw + \
                    '',
                    menu = [['user', get_lang(conn, 'return')]]
                ))
            elif 'c_type' in flask.session and (flask.session['c_key'] == input_key or flask.session['c_key'] == 'email_pass'):
                curs.execute(db_change('select data from other where name = "encode"'))
                db_data = curs.fetchall()
        
                if flask.session['c_type'] == 'register':
                    if flask.session['c_key'] == 'email_pass':
                        flask.session['c_email'] = ''
        
                    curs.execute(db_change("select id from user_set limit 1"))
                    first = 1 if not curs.fetchall() else 0
        
                    curs.execute(db_change("select id from user_set where id = ?"), [flask.session['c_id']])
                    if curs.fetchall():
                        for i in re_set_list:
                            flask.session.pop(i, None)
        
                        return await re_error(conn, 8)
                
                    curs.execute(db_change("select id from user_set where id = ? and name = 'application'"), [flask.session['c_id']])
                    if curs.fetchall():
                        for i in re_set_list:
                            flask.session.pop(i, None)
        
                        return await re_error(conn, 8)
        
                    curs.execute(db_change('select data from other where name = "requires_approval"'))
                    requires_approval = curs.fetchall()
                    if requires_approval and requires_approval[0][0] == 'on':
                        user_app_data = {}
                        user_app_data['id'] = flask.session['c_id']
                        user_app_data['pw'] = flask.session['c_pw']
                        user_app_data['date'] = get_time()
                        user_app_data['encode'] = db_data[0][0]
                        user_app_data['question'] = flask.session['c_que']
                        user_app_data['answer'] = flask.session['c_ans']
                        user_app_data['ip'] = ip
                        user_app_data['ua'] = user_agent
                        user_app_data['email'] = flask.session['c_email']
                        
                        curs.execute(db_change("insert into user_set (id, name, data) values (?, ?, ?)"), [flask.session['c_id'], 'application', json_dumps(user_app_data)])
        
                        for i in re_set_list:
                            flask.session.pop(i, None)
        
                        return redirect(conn, '/application_submitted')
                    else:
                        if first == 0:
                            user_auth = 'user'
                        else:
                            user_auth = 'owner'
                        
                        curs.execute(db_change("insert into user_set (id, name, data) values (?, 'pw', ?)"), [flask.session['c_id'], flask.session['c_pw']])
                        curs.execute(db_change("insert into user_set (id, name, data) values (?, 'acl', ?)"), [flask.session['c_id'], user_auth])
                        curs.execute(db_change("insert into user_set (id, name, data) values (?, 'date', ?)"), [flask.session['c_id'], get_time()])
                        curs.execute(db_change("insert into user_set (id, name, data) values (?, 'encode', ?)"), [flask.session['c_id'], db_data[0][0]])
        
                    curs.execute(db_change("insert into user_set (name, id, data) values ('email', ?, ?)"), [flask.session['c_id'], flask.session['c_email']])
                    ua_plus(conn, flask.session['c_id'], ip, user_agent, get_time())
        
                    flask.session['id'] = flask.session['c_id']
                    flask.session['head'] = ''
                else:
                    curs.execute(db_change('delete from user_set where name = "email" and id = ?'), [ip])
                    curs.execute(db_change('insert into user_set (name, id, data) values ("email", ?, ?)'), [ip, flask.session['c_email']])
        
                    first = 0
        
                for i in re_set_list:
                    flask.session.pop(i, None)
        
                return redirect(conn, '/change') if first == 0 else redirect(conn, '/setting') 
            else:
                for i in re_set_list:
                    flask.session.pop(i, None)
        
                return redirect(conn, '/user')
        else:
            curs.execute(db_change('select data from other where name = "check_key_text"'))
            sql_d = curs.fetchall()
            b_text = (sql_d[0][0] + '<hr class="main_hr">') if sql_d and sql_d[0][0] != '' else ''
        
            return easy_minify(conn, flask.render_template(skin_check(conn),
                imp = [get_lang(conn, 'check_key'), await wiki_set(), await wiki_custom(conn), wiki_css([0, 0])],
                data = '''
                    <form method="post">
                        ''' + b_text + '''
                        <input placeholder="''' + get_lang(conn, 'key') + '''" name="key" type="password">
                        <hr class="main_hr">
                        <button type="submit">''' + get_lang(conn, 'save') + '''</button>
                    </form>
                ''',
                menu = [['user', get_lang(conn, 'return')]]
            ))