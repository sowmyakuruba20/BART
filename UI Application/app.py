from flask import Flask, request, json, render_template
from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("Bart", "Madhu@269"))

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    source=request.form['source']
    destination=request.form['destination']
 
    with driver.session() as session:
        # Query for travel time
        result1 = session.run("MATCH (start:Station {station_id: $source}), (end:Station {station_id: $destination}) "
                              "MATCH path = allShortestPaths((start)-[:travel_time*]->(end)) "
                              "WITH reduce(totalTime = 0, rel in relationships(path) | totalTime + rel.time) as totalTime "
                              "RETURN totalTime",
                              source=source,
                              destination=destination
                             )
        record1 = result1.single()
        if record1:
            total_time = record1['totalTime']
        else:
            total_time = "Not found"

        # Query for fare
        result2 = session.run("MATCH (origin:Station {station_id: $source})-[fare:fare]->(destination:Station {station_id: $destination}) "
                              "RETURN origin.station_name as Source, destination.station_name as Destination, fare.youth_fare as YouthClipper, fare.senior_fare as SeniorDisabledClipper,fare.clipper_start_fare as ClipperStart, fare.clipper_fare as Clipper",
                              source=source,
                              destination=destination
                             )
        record2 = result2.single()
        if record2:
            origin_name = record2['Source']
            destination_name = record2['Destination']
            youth_clipper = record2['YouthClipper']
            senior_disabled_clipper = record2['SeniorDisabledClipper']
            clipper_start = record2['ClipperStart']
            clipper = record2['Clipper']
        else:
            origin_name = "Not found"
            destination_name = "Not found"
            youth_clipper = "Not found"
            senior_disabled_clipper = "Not found"
            clipper_start = "Not found"
            clipper = "Not found"

    return render_template('result.html', total_time=total_time, source=source, destination=destination, origin_name=origin_name, destination_name=destination_name, youth_clipper=youth_clipper, senior_disabled_clipper=senior_disabled_clipper, clipper_start=clipper_start, clipper=clipper)      

@app.route('/bart-extension', methods=['POST'])
def bart(): 
    return render_template('extension.html') 

@app.route('/calculate-extension', methods=['POST'])
def extension_calculate():
    source=request.form['source']
    destination="BERY"  

    with driver.session() as session:
        # Query for travel time
        result1 = session.run("MATCH (start:Station {station_id: $source}), (end:Station {station_id: $destination}) "
                              "MATCH path = allShortestPaths((start)-[:travel_time*]->(end)) "
                              "WITH reduce(totalTime = 0, rel in relationships(path) | totalTime + rel.time) as totalTime "
                              "RETURN totalTime",
                              source=source,
                              destination=destination
                             )
        record1 = result1.single()
        if record1:
            total_time = record1['totalTime']
        else:
            total_time = "Not found"

        # Query for fare
        result2 = session.run("MATCH (origin:Station {station_id: $source})-[fare:fare]->(destination:Station {station_id: $destination}) "
                              "RETURN origin.station_name as Source, destination.station_name as Destination, fare.youth_fare as YouthClipper, fare.senior_fare as SeniorDisabledClipper,fare.clipper_start_fare as ClipperStart, fare.clipper_fare as Clipper",
                              source=source,
                              destination=destination
                             )
        record2 = result2.single()
        if record2:
            origin_name = record2['Source']
            destination_name = record2['Destination']
            youth_clipper = record2['YouthClipper']
            senior_disabled_clipper = record2['SeniorDisabledClipper']
            clipper_start = record2['ClipperStart']
            clipper = record2['Clipper']
        else:
            origin_name = "Not found"
            destination_name = "Not found"
            youth_clipper = "Not found"
            senior_disabled_clipper = "Not found"
            clipper_start = "Not found"
            clipper = "Not found"

    return render_template('bart.html', total_time=total_time, source=source, destination="SJSU", origin_name=origin_name, destination_name="SJSU", youth_clipper=youth_clipper, senior_disabled_clipper=senior_disabled_clipper, clipper_start=clipper_start, clipper=clipper)      

 
if __name__ == '__main__':
    app.run(debug=True)


    

