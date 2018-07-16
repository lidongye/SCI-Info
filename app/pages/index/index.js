//index.js
//获取应用实例
const app = getApp();

Page({
  data: {
    journal_name: '',
    gt: null,
    lt: null,
    index : 1,
    page_size : 10,
    num : 20,
    pages : [1,2,3,4,5],
    order_by : 'IF',
    order_type : "DESC",
    SCIInfo : app.SCIInfo,
    totalPage : 0
  },
  //事件处理函数
  show_table: function (data) {
    //更新页面数据
    console.log(data)
    this.setData({
        SCIInfo:data.data
      })
  },
  bindNameInput(event) {
    // 将用户输入的期刊名与页面变量进行绑定
    this.setData({
      journal_name: event.detail.value,
    })
  },
  bindgtInput(event){
    //大于此IF值
    this.setData({
      gt:event.detail.value
    })
  },
  bindltInput(event) {
    //小于此IF值
    this.setData({
      lt: event.detail.value
    })
  },
  querySCIInfo(){
    //期刊信息查询
    app.getSCIInfo(this.data.journal_name, this.data.gt, this.data.lt, this.data.index, this.data.page_size, this.data.order_by, this.data.order_type, this.show_table)
  },
  goto_page(index){
    //翻页方法，未写
  },
  onLoad: function () {
    //初始化方法
    app.getSCIInfo(this.data.journal_name, this.data.gt, this.data.lt, this.data.index, this.data.page_size, this.data.order_by, this.data.order_type, this.show_table)
  }
})
