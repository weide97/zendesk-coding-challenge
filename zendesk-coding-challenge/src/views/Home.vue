<template>
  <div class="home">
      <h1>Mobile Ticket Viewer</h1>
      <div v-if="main">
        <p v-if="error">{{this.message}}</p>
        <div v-else>
          <p>{{this.message}}</p>
          <div >
          <table class='table table-bordered' >
            <tr>
              <th >
                Status
              </th>
              <th >
                Title
              </th>
            </tr>
            <tr v-for="(ticket_detail, index) in ticket_info" :key="index">
              <td  v-on:click="getTicketInfo(index)">{{ticket_detail.status}}</td>
              <td  v-on:click="getTicketInfo(index)">{{ticket_detail.raw_subject}}</td>
            </tr>
          </table> 
          </div> 
        </div>
      <button type="button" class="btn btn-primary"  :disabled="backPage==null" v-on:click="new_page(backPage)">Back</button>
      <button type="button" class="btn btn-primary" :disabled="nextPage==null" v-on:click="new_page(nextPage)">Next</button>    
    </div>

    <div v-if="!main">
    
    <h4>Requester: {{this.requestor}}</h4>
    <h2>Subject: {{this.subject}}</h2>
    <h4>Detials: {{this.detail}}</h4>
    <button type="button" class="btn btn-primary" v-on:click="ticket_page()">Back to tickets</button>
    </div>
  </div>
</template>

<style scoped>
 th,td{
    padding: 10px 15px;
    font-size: 14px;
    text-align: left;
    border: 1px solid black;
    margin-left: auto;
    margin-right: auto;
    width:40%
 }
</style>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  data(){
    return{
      // main ticket page
      ticket_info: '',
      error: false,
      message: '',
      backPage: '',
      nextPage: '',
      // ticket detail
      main: true,
      requestor: '', 
      subject: '',
      detail: ''
      
    }
  },
  mounted(){
    axios.get("http://127.0.0.1:5000/getTicket")
      .then(res=>{
        console.log(res.data.data)
        var all_info = res.data.data
        var total_ticket = all_info["count"]
        var page_ticket = all_info["tickets"].length
        this.ticket_info = all_info["tickets"]
        this.nextPage = all_info['next_page']
        this.backPage = all_info['previous_page']
        console.log("backPage")
        this.message = total_ticket + " total tickets, "+ page_ticket + " on this page"
      }).catch(()=>{
        this.error = true
        this.message = "Error: Couldn't Authenticate You"
      })

    },
  methods:{
    new_page(url){
    axios.post("http://127.0.0.1:5000/getTicketByPage",{url:url})
      .then(res=>{
        console.log(res.data.data)
        var all_info = res.data.data
        var total_ticket = all_info["count"]
        var page_ticket = all_info["tickets"].length
        this.ticket_info = all_info["tickets"]
        this.nextPage = all_info['next_page']
        this.backPage = all_info['previous_page']
        console.log("backPage")
        this.message = total_ticket + " total tickets, "+ page_ticket + " on this page"
      }).catch(()=>{
        this.error = true
        this.message = "Error: Couldn't Authenticate You"
      })

     },
    ticket_page(){
      this.main = true
    }, 
    getTicketInfo(ind){
      this.main=false
      console.log(this.ticket_info[ind])
      var specific_ticket = this.ticket_info[ind]
      console.log(specific_ticket["requester_id"])
      axios.post("http://127.0.0.1:5000/userIdentity",{id:specific_ticket["requester_id"]})
        .then(res =>{
          var user_info = res.data.data
          this.requestor = user_info["identities"][0]["value"]
        })
        .catch(()=>{
          this.requestor = "Error"
        })
      this.subject= specific_ticket["subject"]
      this.detail = specific_ticket["description"]
    }
  }
  }

</script>
