//left pad number n with '0' to meet with the given lenght width
function lpad(n, width) {
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join('0') + n;
}
week_zh = new Array("日", "一", "二", "三", "四", "五", "六");

function startTime() {
    cur_date = new Date();
    // set current date and week
    document.getElementById("date").innerHTML =
            (cur_date.getYear() + 1900).toString() + "年"
            + lpad(cur_date.getMonth() + 1, 2) + "月"
            + lpad(cur_date.getDate(), 2) + "日"
            + " 星期" + week_zh[cur_date.getDay()];
    // set current time
    document.getElementById("time").innerHTML =
            lpad(cur_date.getHours(), 2) + ":"
            + lpad(cur_date.getMinutes(), 2) + ":"
            + lpad(cur_date.getSeconds(), 2);
    t = setTimeout(function(){
        startTime();
    }, 500)
}

startTime();
