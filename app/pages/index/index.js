//index.js
//获取应用实例
const app = getApp();

Page({
  data: {
    journal_name: '',
    gt: null,
    lt: null,
    page_index: 1,
    page_size: 10,
    order_by: 'IF',
    order_type: "DESC",
    SCIInfo: [],
    has_more_data: true,
    hidden_modal: true,
    modal_data: {},
    info_list: [
      {
        "title": "Full Title",
        "field": "title",
        "description": "期刊名全名"
      },
      {
        "title": "Abbreviated",
        "field": "abbreviated",
        "description": "期刊名简写"
      },
      {
        "title": "ISSN",
        "field": "ISSN",
        "description": "ISSN"
      },
      {
        "title": "Total Cites",
        "field": "total_cites",
        "description": "总被引用次数"
      },
      {
        "title": "Impact Factor(IF)",
        "field": "IF",
        "description": "影响因子"
      },
      {
        "title": "IF without Self Cites",
        "field": "IF_without_self_cites",
        "description": "除自引外影响因子"
      },
      {
        "title": "5 Year IF",
        "field": "IF_5_year",
        "description": "近五年影响因子"
      },
      {
        "title": "Immediacy Index",
        "field": "immediacy_index",
        "description": "及时指数"
      },
      {
        "title": "Citable Items",
        "field": "citable_items",
        "description": "当年文章数"
      },
      {
        "title": "Cited Half-Life",
        "field": "cited_half_life",
        "description": "被引半衰期"
      },
      {
        "title": "Citing Half-life",
        "field": "citing_half_life",
        "description": "引用半衰期"
      },
      {
        "title": "Eigenfactor Score",
        "field": "eigenfactor_score",
        "description": ""
      },
      {
        "title": "Influence Score",
        "field": "influence_score",
        "description": ""
      },
      {
        "title": "% Articles in Citable Items",
        "field": "articles_in_citable_items",
        "description": ""
      },
      {
        "title": "Average Journal \ Impact Factor Percentile",
        "field": "ajifp",
        "description": ""
      },
      {
        "title": "Normalized Eigenfactor",
        "field": "normalized_eigenfactor",
        "description": ""
      }
    ]
  },
  //事件处理函数
  getSCIInfo: function() {
    //期刊信息查询
    var that = this
    wx.showLoading({
      title: '正在加载数据,',
    })
    wx.request({
      url: 'https://sciif.soyomics.com/if',
      data: {
        "title": this.data.journal_name,
        "gt": this.data.gt,
        "lt": this.data.lt,
        "page_size": this.data.page_size,
        "page_index": this.data.page_index,
        "order_by": this.data.order_by,
        "order_type": this.data.order_type
      },
      method: "GET",
      success: function(res) {
        wx.hideLoading()
        console.log(res.data)
        if (res.data.status == 200) {
          if (res.data.data.length < that.data.page_size) {
            that.setData({
                SCIInfo: that.data.SCIInfo.concat(res.data.data),
                has_more_data: false,
              }),
              wx.showToast({
                title: '无更多数据',
              })
          } else {
            that.setData({
              SCIInfo: that.data.SCIInfo.concat(res.data.data),
              page_index: that.data.page_index + 1,
              has_more_data: true,
            })
          }
        } else {
          wx.showToast({
            title: '网络连接错误',
          })
        }
      },
      fail: function() {
        wx.hideLoading()
      }
    })
  },
  bindNameInput(event) {
    // 将用户输入的期刊名与页面变量进行绑定
    this.setData({
      journal_name: event.detail.value,
    })
  },
  bindgtInput(event) {
    //大于此IF值
    this.setData({
      gt: event.detail.value
    })
  },
  bindltInput(event) {
    //小于此IF值
    this.setData({
      lt: event.detail.value
    })
  },
  querySCIInfo: function() {
    this.setData({
      page_index: 1,
      SCIInfo: []
    })
    this.getSCIInfo()
  },
  onLoad: function() {
    //初始化方法
    this.data.page_index = 1,
      this.querySCIInfo()
  },
  onReachBottom: function() {
    if (this.data.has_more_data) {
      this.getSCIInfo()
    }
  },
  showSCIInfo: function(e) {
    var that = this
    that.setData({
      modal_data: that.data.SCIInfo[e.currentTarget.dataset.key],
      hidden_modal: false
    })
  },
})