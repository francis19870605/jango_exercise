/**
 * Created by francis on 2017/9/4.
 */

function showModel() {
    document.getElementById('pop').classList.remove('show_hide');
    document.getElementById('hid').classList.remove('show_hide');
}

function hideModel() {
    document.getElementById('hid').classList.add('show_hide');
    document.getElementById('pop').classList.add('show_hide');
}

function SelectAll() {
    var tab_result = document.getElementById('table_select');
    var tr_list = tab_result.children;
    for(var i=0; i<tr_list.length; i++){
        var current_tr = tr_list[i];
        var checkbox = current_tr.children[0].children[0];
        checkbox.checked = true;
    }
}

function ReverseAll() {
    var tab_result = document.getElementById('table_select');
    var tr_list = tab_result.children;
    for(var i=0; i<tr_list.length; i++){
        var current_tr = tr_list[i];
        var checkbox = current_tr.children[0].children[0];
        if(checkbox.checked == true){
            checkbox.checked = false;
        }else {
            checkbox.checked = true;
        }
    }
}

function CancelAll() {
    var tab_result = document.getElementById('table_select');
    var tr_list = tab_result.children;
    for(var i=0; i<tr_list.length; i++){
        var current_tr = tr_list[i];
        var checkbox = current_tr.children[0].children[0];
        checkbox.checked = false;
    }
}

function ShowHide(menu_id) {
    var current_header = document.getElementById(menu_id);
    var item_list = current_header.parentElement.parentElement.children;
    for(var i=0;i<item_list.length;i++){
        var current_item = item_list[i];
        var current_menu = current_item.children[1];
        //console.log(current_menu);
        current_menu.classList.add('hide');
    }
    current_header.nextElementSibling.classList.remove('hide');
}



















