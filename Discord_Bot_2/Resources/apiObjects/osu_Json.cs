using System;
using System.Collections.Generic;
using System.Text;

namespace Discord_Bot.Resources.apiObjects
{
    class osu_Json
    {
        public osu_Json() { }

        public string userid { get; set; }
        public string username { get; set; }
        public string count300 { get; set; }
        public string count100 { get; set; }
        public string count50 { get; set; }
        public string playcount { get; set; }
        public string ranked_score { get; set; }
        public string total_score { get; set; }
        public string pp_rank { get; set; }
        public string level { get; set; }
        public string pp_raw { get; set; }
        public string accuracy { get; set; }
        public string count_rank_ss { get; set; }
        public string count_rank_s { get; set; }
        public string count_rank_a { get; set; }
        public string country { get; set; }
        public string pp_country_rank { get; set; }
    }
}
