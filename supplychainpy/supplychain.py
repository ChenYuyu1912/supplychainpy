#!/usr/bin/env python3
import os
from decimal import Decimal
from supplychainpy.demand.summarise import OrdersAnalysis
import time

from supplychainpy import simulate
from supplychainpy import model_inventory
from supplychainpy.demand.summarise import OrdersAnalysis

__author__ = 'kevin'


def main():
    start_time = time.time()

    orders_analysis = [analysis for analysis in
                       model_inventory.analyse_orders_abcxyz_from_file(file_path="data2.csv", z_value=Decimal(1.28),
                                                                       reorder_cost=Decimal(5000), file_type="csv",
                                                                       length=12)]

    summary = OrdersAnalysis(analysed_orders=orders_analysis)
    abc_raw = summary.abc_xyz_raw

    #for analysis in summary.abc_xyz_summary():
    #    print(analysis)

    #for top_shortages in summary.top_sku(attribute="shortages", count=10, reverse=False):
    #    print(top_shortages)
    #get sku keys from category analysis and unpack for describe sku
    questions = ['KR202-209', 'KR202-210', 'KR202-211']
    for summarised in summary.describe_sku('KR202-210'):
        print(summarised)
    #print("keys {}".format(list(ax_shortages.keys())))
    #print("values {}".format(list(ax_shortages.values())))

    # top_ten_shortages = [item for item in
    #                     SKU(analysed_orders=orders_analysis.orders).top_sku(attribute="shortage", count=10,
    #                                                                         reverse=True)]
    #
    # top_ten_excess = [item for item in
    #                  SKU(analysed_orders=orders_analysis.orders).top_sku(attribute="excess_stock", count=10,
    #                                                                      reverse=True)]
    #
    # for order in SKU(analysed_orders=orders_analysis.orders).top_sku(attribute="shortage", count=10, reverse=False):
    #    print(order)
    #
    #
    #

    #sim_window = simulate.summarize_window(simulation_frame=sim, period_length=12)
    #
    # sim_frame = simulate.summarise_frame(sim_window)
    #
    # optimised_orders = simulate.optimise_service_level(service_level=95.0, frame_summary=sim_frame,
    #                                                   orders_analysis=orders_analysis.orders, runs=100,
    #                                                   percentage_increase=1.30)
    #
    # sim_frame = simulate.summarise_frame(sim_window)
    #
    # optimised_orders = simulate.optimise_service_level(service_level=95.0, frame_summary=sim_frame,
    #                                                   orders_analysis=orders_analysis.orders, runs=100,
    #                                                   percentage_increase=1.30)
    # end = time.time()
    #
    # secs = end - start_time
    # print(secs)


if __name__ == '__main__':
    main()
