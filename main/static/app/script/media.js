$("document").ready(()=>{
    function set_media(type){
        //TODO: добавить изменение стилей переключателя
        $('.selected-media').removeClass('selected-media');
        $(`.${type}-list`).addClass('selected-media');
    }
    $(".media-type").click((event)=>{
        set_media(event.currentTarget.href.split('#')[1])
    })
});