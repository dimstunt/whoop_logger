### What bot needs to do:
* save daily events
* make an aggregation about yesterday in web (auth?)
* take info from whoop api and show it
* smthing from ml


### plan
- [x] Add postgres and pgadmin via docker-compose
- [ ] Add model into postgres
  - [ ] event_type
  - [ ] event
- [ ] Add API to save an event into postgres
- [ ] Add API to delete last event in postgres
- [ ] move model and schema to fstapi
- [ ] Add API route to agregation last day
- [ ] Change docker-compose to k8s
- [ ] Add saving event via telegram bot
- [ ] Add web stat
- [ ] Add auth into web
- [ ] Add auth via telegram
