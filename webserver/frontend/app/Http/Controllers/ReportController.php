<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Report;

class ReportController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Report::all();
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'id' => 'nullable|integer',
            'company_name' => 'nullable|string|max:255',
            'robot_model' => 'nullable|string|max:255',
            'map' => 'nullable|string|max:255',
            'route' => 'nullable|string|max:255',
            'orientations_tried' => 'nullable|integer',
            'runs' => 'nullable|integer',
            'confidence' => 'nullable|numeric|between:0,1',
            'time_spent' => 'nullable|integer',
            'predicted_route_time' => 'nullable|integer',
            'boxes_moved_per_run' => 'nullable|integer',
        ]);

        $report = Report::create([
            'id' => $validatedData['id'] ?? null, // Set 'id' manually if present
            'company_name' => $validatedData['company_name'],
            'robot_model' => $validatedData['robot_model'],
            'map' => $validatedData['map'],
            'route' => $validatedData['route'],
            'orientations_tried' => $validatedData['orientations_tried'] ?? 0,
            'runs' => $validatedData['runs'] ?? 0,
            'confidence' => $validatedData['confidence'] ?? 0,
            'time_spent' => $validatedData['time_spent'] ?? 0,
            'predicted_route_time' => $validatedData['predicted_route_time'] ?? 0,
            'boxes_moved_per_run' => $validatedData['boxes_moved_per_run'] ?? 0,
        ]);

        // $report = Report::create($validatedData);
        return response()->json($report, 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        $report = Report::findOrFail($id); // Find the Report by ID

        $validatedData = $request->validate([
            'company_name' => 'nullable|string|max:255',
            'robot_model' => 'nullable|string|max:255',
            'map' => 'nullable|string|max:255',
            'route' => 'nullable|string|max:255',
            'orientations_tried' => 'nullable|integer',
            'runs' => 'nullable|integer',
            'confidence' => 'nullable|numeric|between:0,1',
            'time_spent' => 'nullable|numeric',
            'predicted_route_time' => 'nullable|numeric',
            'boxes_moved_per_run' => 'nullable|integer',
        ]);

        $report->update($validatedData); // Update with partial data
        return response()->json($report, 200); // Return the updated Report
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
