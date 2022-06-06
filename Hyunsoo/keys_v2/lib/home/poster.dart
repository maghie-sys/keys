
import 'package:flutter/cupertino.dart';
import 'package:keys_v2/Screens/detail_screen3.dart';

class Poster extends StatelessWidget{

  Poster({Key key, this.posterUrl}) : super(key: key);

  final String posterUrl;


  @override
  Widget build(BuildContext context) {
    return Padding(padding: const EdgeInsets.only(right: 10.0),
    /*child: GestureDetector(
      behavior: HitTestBehavior.translucent,
      onTap: () {
        Navigator.pushNamed(context, DetailScreen.routeName, arguments: DetailScreen(posterUrl: posterUrl));
      },*/
    child: ClipRRect(
      borderRadius: BorderRadius.circular(5.0),
      child: Image(
        image: AssetImage(posterUrl),
        fit: BoxFit.cover,
        width: 120.0,
        height: 200.0,
      ),
    ),
 //   ),
    );
  }
}