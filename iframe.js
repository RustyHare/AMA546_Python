function listenerResizeIframeHeightToInnerContent() {
    let iframes = document.querySelectorAll('iframe');
    iframes.forEach(iframe => {
        iframe.contentWindow.postMessage('getHeight', '*') + "px";

    });
    setTimeout(listenerResizeIframeHeightToInnerContent, 50);
}
window.addEventListener("message", (event) => {
    let iframes = document.querySelectorAll('iframe');
    iframes.forEach(iframe => {
        if(event.source === iframe.contentWindow){
            iframe.style.height = (event.data + 20).toString() + "px";
        }
    });
})
if (window.addEventListener != null) {

    window.addEventListener("load", listenerResizeIframeHeightToInnerContent, false);



} else if (window.attachEvent != null) {

    window.attachEvent("onload", listenerResizeIframeHeightToInnerContent);

}