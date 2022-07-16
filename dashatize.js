function dashatize(num) {
  return (num+'').replace(/([13579])/g,'-$1-').replace(/\-\-/g, '-').replace(/^\-|\-$/g, '');
}


dashatize(274)
// '2-7-4'
dashatize(6815)
// '68-1-5'
