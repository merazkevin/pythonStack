// Given in an alumni interview in 2021.
// String Encode
// You are given a string that may contain sequences of consecutive characters.
// Create a function to shorten a string by including the character,
// then the number of times it appears. 

// If final result is not shorter (such as "bb" => "b2" ),
// return the original string.
// */

const str1 = "aaaabbcddd";
const expected1 = "a4bbcd3";
const expected1b = "a4b2cd3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

const str5 = "abbbbbbbbbbbbbbbbb"
const expected5 = "ab17"
