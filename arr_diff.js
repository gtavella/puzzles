/*
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
*/


function arrayDiff(a, b) { return a.filter(e => { return b.indexOf(e) === -1 }); }

arrayDiff([1,2,2,2,3],[2])
// [1, 3]
