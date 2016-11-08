/*----------------------- Add button to show preview -------------------------*/
var code_blocks = document.querySelectorAll(".code-block");
for (var i = 0; i < code_blocks.length; ++i) {
    var code_block = code_blocks[i];
    code_block.outerHTML =
        '<button type="button" class="btn btn-info show-block-btn">预览</button>'
        + code_block.outerHTML;
}
$('.show-block-btn').click(function(){
    $(this).next('.code-block').slideToggle();
});


/*--------------------------- Show date and time --------------------------------------*/
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


/*--------------------------- Auto generate Catalog --------------------------*/
function scrollView(title_id) {
    var target = $("#" + title_id);
    $('html, body').animate({
        scrollTop: target.offset().top - 70
    }, "slow", function() {
        target.addClass('flash').delay(1600).queue(function() {
            $(this).removeClass('flash').dequeue();
        });
    });
}

var intro_blocks = document.getElementsByClassName('intro-block');
var catalog_part = document.getElementById('catalog-part');
catalog_part.innerHTML = "";
for (i = 0; i < intro_blocks.length; ++i) {
    intro_block_h2 = intro_blocks[i].getElementsByTagName('h2')[0];
    intro_block_h2.id = "title-" + i.toString();
    catalog_part.innerHTML += '<a href="#" class="catalog-title" '
                             + 'onclick="scrollView(' + "'"
                             + intro_block_h2.id + "'" + '); return false;">'
                             + intro_block_h2.innerText + '</a><br/>';

    intro_block_h3s =  intro_blocks[i].getElementsByTagName('h3');
    for (j = 0; j < intro_block_h3s.length; ++j) {
        intro_block_h3 = intro_block_h3s[j];
        intro_block_h3.id = "title-" + i.toString() + j.toString();
        catalog_part.innerHTML += '<a href="#" class="catalog-subtitle" '
                                 + 'onclick="scrollView(' + "'"
                                 + intro_block_h3.id + "'" + '); return false;">'
                                 + intro_block_h3.innerText + '</a><br/>';
    }
}

/*--------------------------- Go to top --------------------------*/
document.getElementById('go-to-top').onclick = function(){
    $('html, body').animate({ scrollTop: 0 }, 'fast');
}

$("#go-to-top").hide();
$(window).scroll(function() {
    if ($(window).scrollTop() > 300) {
        $("#go-to-top").fadeIn("slow");
    }
    else {
        $("#go-to-top").fadeOut("fast");
    }
});
