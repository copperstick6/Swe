const _ = require('lodash')
function RMSE(input, expected){

  var new_map = _.map(_.range(input.length), function(sum, current){
	  return Math.pow(input[current] - expected[current], 2)
  })
  return Math.pow( _.reduce(new_map, function(cur_sum, current){
	  return cur_sum + current
  }, 0)/input.length, 1/2)
}

console.log(RMSE([1,2], [3,4]))



class range_iterator{
	constructor(a, b){
		this.a = a
		this.b = b
	}

	[Symbol.iterator](){
		return this;
	}

	next(){
		let n  = {"value": this.a, "done": this.a === this.b}
		++this.a;
		return n;
	}
}
