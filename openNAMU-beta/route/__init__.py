from route.api_image_view import api_image_view
from route.api_skin_info import api_skin_info
from route.api_user_info import api_user_info
from route.api_version import api_version

from route.bbs_w_edit import bbs_w_edit
from route.bbs_make import bbs_make
# from route.bbs_w_hide import bbs_w_hide
from route.bbs_w_pinned import bbs_w_pinned
from route.bbs_w_delete import bbs_w_delete
from route.bbs_w import bbs_w
from route.bbs_delete import bbs_delete
# from route.bbs_hide import bbs_hide
from route.bbs_w_post import bbs_w_post
from route.bbs_w_comment_tool import bbs_w_comment_tool
from route.bbs_w_tool import bbs_w_tool

from route.edit import edit
from route.edit_backlink_reset import edit_backlink_reset
from route.edit_delete import edit_delete
from route.edit_delete_file import edit_delete_file
from route.edit_delete_multiple import edit_delete_multiple
from route.edit_move import edit_move
from route.edit_revert import edit_revert
from route.edit_upload import edit_upload
from route.edit_request import edit_request

from route.filter_all import filter_all
from route.filter_all_add import filter_all_add
from route.filter_all_delete import filter_all_delete

from route.give_admin_groups import give_admin_groups
from route.give_delete_admin_group import give_delete_admin_group
from route.give_user_ban import give_user_ban
from route.give_user_fix import give_user_fix

from route.list_acl import list_acl
from route.list_admin import list_admin
from route.list_admin_auth_use import list_admin_auth_use
from route.list_old_page import list_old_page
from route.list_admin_group import list_admin_group
from route.list_image_file import list_image_file
from route.list_long_page import list_long_page
from route.list_no_link import list_no_link
from route.list_please import list_please
from route.list_title_index import list_title_index
from route.list_user import list_user
from route.list_user_check import list_user_check
from route.list_user_check_delete import list_user_check_delete
from route.list_history import list_history

from route.login_find import login_find
from route.login_find_email import login_find_email
from route.login_find_email_check import login_find_email_check
from route.login_find_key import login_find_key
from route.login_login import login_login
from route.login_login_2fa import login_login_2fa
from route.login_login_2fa_email import login_login_2fa_email
from route.login_logout import login_logout

from route.login_register import login_register
from route.login_register_email import login_register_email
from route.login_register_email_check import login_register_email_check
from route.login_register_submit import login_register_submit

from route.main_func_error_404 import main_func_error_404

from route.main_search import main_search
from route.main_search_deep import main_search_deep
from route.main_search_goto import main_search_goto

from route.main_setting import main_setting
from route.main_setting_external import main_setting_external
from route.main_setting_head import main_setting_head
from route.main_setting_main import main_setting_main
from route.main_setting_main_logo import main_setting_main_logo
from route.main_setting_phrase import main_setting_phrase
from route.main_setting_robot import main_setting_robot
from route.main_setting_sitemap import main_setting_sitemap
from route.main_setting_sitemap_set import main_setting_sitemap_set
from route.main_setting_skin_set import main_setting_skin_set
from route.main_setting_top_menu import main_setting_top_menu
from route.main_setting_email_test import main_setting_email_test

from route.main_sys_restart import main_sys_restart
from route.main_sys_shutdown import main_sys_shutdown
from route.main_sys_update import main_sys_update

from route.main_tool_admin import main_tool_admin
from route.main_tool_other import main_tool_other
from route.main_tool_redirect import main_tool_redirect

from route.main_view import main_view
from route.main_view_file import main_view_file
from route.main_view_image import main_view_image

from route.recent_app_submit import recent_app_submit

from route.recent_change import recent_change
from route.recent_edit_request import recent_edit_request
from route.recent_history_add import recent_history_add
from route.recent_history_delete import recent_history_delete
from route.recent_history_hidden import recent_history_hidden
from route.recent_history_reset import recent_history_reset
from route.recent_history_send import recent_history_send
from route.recent_history_tool import recent_history_tool
from route.recent_record_reset import recent_record_reset
from route.recent_record_topic import recent_record_topic

from route.topic import topic
from route.topic_comment_blind import topic_comment_blind
from route.topic_comment_delete import topic_comment_delete
from route.topic_comment_notice import topic_comment_notice
from route.topic_comment_tool import topic_comment_tool
from route.topic_tool import topic_tool
from route.topic_tool_acl import topic_tool_acl
from route.topic_tool_change import topic_tool_change
from route.topic_tool_delete import topic_tool_delete
from route.topic_tool_setting import topic_tool_setting

from route.user_alarm import user_alarm
from route.user_alarm_delete import user_alarm_delete
from route.user_challenge import user_challenge
from route.user_count import user_count
from route.user_info import user_info
from route.user_edit_filter import user_edit_filter

from route.user_setting import user_setting
from route.user_setting_email import user_setting_email
from route.user_setting_email_check import user_setting_email_check
from route.user_setting_email_delete import user_setting_email_delete
from route.user_setting_head import user_setting_head
from route.user_setting_head_reset import user_setting_head_reset
from route.user_setting_key import user_setting_key
from route.user_setting_key_delete import user_setting_key_delete
from route.user_setting_pw import user_setting_pw
from route.user_setting_skin_set import user_setting_skin_set
from route.user_setting_skin_set_main import user_setting_skin_set_main
from route.user_setting_top_menu import user_setting_top_menu
from route.user_setting_user_name import user_setting_user_name

from route.user_watch_list import user_watch_list
from route.user_watch_list_name import user_watch_list_name

from route.view_set import view_set
from route.view_diff import view_diff
from route.view_down import view_down
from route.view_raw import view_raw
from route.view_w_raw import view_w_raw
from route.view_w import view_w
from route.view_xref import view_xref
from route.view_random import view_random

from route.vote_add import vote_add
from route.vote_close import vote_close
from route.vote_end import vote_end
from route.vote_list import vote_list
from route.vote_select import vote_select

from route.n_list_recent_discuss import list_recent_discuss
from route.n_list_recent_block import list_recent_block
from route.n_list_user_check_submit import list_user_check_submit

from route.n_w_watch_list import w_watch_list

from route.n_topic_list import topic_list

from route.n_give_auth import give_auth

from route.n_setting_404_page import setting_404_page

from route.n_bbs_main import bbs_main
from route.n_bbs_in import bbs_in
from route.n_bbs_w_set import bbs_w_set

from route.n_edit_move_all import edit_move_all

from route.go_api_func_llm import api_func_llm
from route.go_api_func_language import api_func_language
from route.go_api_func_sha224 import api_func_sha224
from route.go_api_func_ip import api_func_ip
from route.go_api_func_ip_menu import api_func_ip_menu
from route.go_api_func_auth import api_func_auth
from route.go_api_func_email import api_func_email, api_func_email_exter
from route.go_api_func_search import api_func_search, api_func_search_exter

from route.go_api_give_auth import api_give_auth

from route.go_api_list_recent_change import api_list_recent_change, api_list_recent_change_exter
from route.go_api_list_recent_discuss import api_list_recent_discuss
from route.go_api_list_recent_block import api_list_recent_block
from route.go_api_list_recent_edit_request import api_list_recent_edit_request, api_list_recent_edit_request_exter
from route.go_api_list_old_page import api_list_old_page, api_list_old_page_exter
from route.go_api_list_title_index import api_list_title_index
from route.go_api_list_acl import api_list_acl
from route.go_api_list_auth import api_list_auth
from route.go_api_list_markup import api_list_markup
from route.go_api_list_history import api_list_history, api_list_history_exter

from route.go_api_bbs import api_bbs
from route.go_api_bbs_list import api_bbs_list
from route.go_api_bbs_w import api_bbs_w
from route.go_api_bbs_w_set import api_bbs_w_set
from route.go_api_bbs_w_tabom import api_bbs_w_tabom
from route.go_api_bbs_w_comment import api_bbs_w_comment, api_bbs_w_comment_exter
from route.go_api_bbs_w_comment_one import api_bbs_w_comment_one, api_bbs_w_comment_one_exter

from route.go_api_setting import api_setting

from route.go_api_topic import api_topic
from route.go_api_topic_list import api_topic_list

from route.go_api_user_rankup import api_user_rankup
from route.go_api_user_setting_editor import api_user_setting_editor

from route.go_api_w_raw import api_w_raw, api_w_raw_exter
from route.go_api_w_random import api_w_random, api_w_random_exter
from route.go_api_w_xref import api_w_xref
from route.go_api_w_watch_list import api_w_watch_list
from route.go_api_w_render import api_w_render, api_w_render_exter
from route.go_api_w_set_reset import api_w_set_reset
from route.go_api_w_page_view import api_w_page_view

from route.go_main_func_easter_egg import main_func_easter_egg