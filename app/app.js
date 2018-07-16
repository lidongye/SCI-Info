//app.js
App({
  onLaunch: function () {
    // 展示本地存储能力
  },
  getSCIInfo(title, gt, lt, page_index, page_size, order_by, order_type, call_back){
    wx.request({
      url: 'https://sciif.soyomics.com/if',
      data:{
        "title" : title,
        "gt" : gt,
        "lt" : lt,
        "page_size" : page_size, 
        "page_index" : page_index,
        "order_by" : order_by, 
        "order_type": order_type
      },
      method:"GET",
      success:function(res){
        call_back(res.data)
      }
    })
  },
  globalData: {
    SCIInfo: null
  }
})